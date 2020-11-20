from services.ali_services import AliApi
from services.cdek_services import CdekAPI, Calc_tarif
from services.pochta_services import PochtaApi
from services.yandex_services import Geocoder
from abc import ABC, abstractmethod
from .models import AliProducts, AliOrders, AliOrdersProductList, AliGroupList, AliChildGroupList, AliOrdersAddInformation
from datetime import datetime, timedelta
from djmoney.money import Money
import re

# ключи Али
appAliKey='31102380'
Alisecret='ea36c75363323184e6779cff827368d4'
AlisSessionKey='50000000b46gvlSAoYNrD9bGtGosBVRl9gEyhqRvenhMpaltVZEzoLTORH13ec5298w'

# сдэк
Account='0372b3fff5d6707cd1633469403952df'
Secure_password='afc14015cce5555ce582bf97b963d2d2'

# ключи Почты РФ
tokenPochta='IomDCsxKO_jjc3yx7eocmSZ3FYDIMMGn'
loginPochta='andrewerm@yandex.ru'
secretPochta='531930Ab-'

def check_funcs(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        print('начало выполнения '+func.__name__)
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'конец выполнения {func.__name__}, время выполнения: {round(end-start)} секунд.')
        return return_value
    return wrapper



class AliDataIterations(ABC):
    def __iter__(self):
        return self

    @abstractmethod
    def __load_data__(self):
        pass

    def __delta_time__(self, depthUpdatingDays, delta):
        u = datetime.utcnow()
        delta = timedelta(days=depthUpdatingDays, hours=delta) # снимаем разницу во времени с UTC
        return u-delta

    def __len__(self):
        return self.total_count

    def __init__(self, methodAli, depthUpdatingDays=None):
        self.method=methodAli
        self.current_page = 1
        self.current_item=-1
        self.depthUpdatingDays=depthUpdatingDays
        self.__load_data__(1, 10)

    def __next__(self):
        if not self.total_count:
            raise StopIteration
        while self.current_page <= self.total_page:
            while self.current_item < self.page_size - 1:
                self.current_item += 1
                return self.data[self.current_item]
            self.current_page += 1
            if self.current_page > self.total_page:
                raise StopIteration
            self.__load_data__(self.current_page, 10)
            self.current_item = -1


class iterOrderList(AliDataIterations):

    def __load_data__(self, page, count):
        res = self.method(page, count, self.__delta_time__(self.depthUpdatingDays, 7))
        self.total_count = res['aliexpress_solution_order_get_response']['result']['total_count']
        self.total_page = res['aliexpress_solution_order_get_response']['result']['total_page']
        if self.total_count:
            self.data=res['aliexpress_solution_order_get_response']['result']['target_list']['order_dto']
            self.page_size = len(self.data)

@check_funcs
class iterProductList(AliDataIterations):
    def __load_data__(self, page, count):
        res = self.method(page, count, self.__delta_time__(self.depthUpdatingDays, -8))
        self.total_count = res['aliexpress_solution_product_list_get_response']['result']['product_count']
        self.total_page = res['aliexpress_solution_product_list_get_response']['result']['total_page']
        if self.total_count:
            self.data=res['aliexpress_solution_product_list_get_response']['result']['aeop_a_e_product_display_d_t_o_list']['item_display_dto']
            self.page_size = len(self.data)

class iterGroupList(AliDataIterations):
    def __load_data__(self, page, count):
        res=self.method()
        self.total_count=1
        self.total_page=1
        self.data = res['aliexpress_product_productgroups_get_response']['result']['target_list']['aeop_ae_product_tree_group']
        self.page_size = len(self.data)

class orderAliInfo():
    def __init__(self, order_id):
        self.order_id=order_id
        #self.aliorder=AliOrdersAddInformation
        self.aliorderdetailed=AliOrdersAddInformation.objects.get_or_create(order_id=self.order_id)[0]
        # self.aliorderproducts=AliOrdersProductList.objects.get(main_order=self.order_id)
        self.aliAPIsession = AliApi(app_key=appAliKey, secret=Alisecret, sessionkey=AlisSessionKey)
        self.__fieldsAliOrders__=[i.name for i in AliOrders._meta.get_fields()]
        self.__fieldsAliOrdersAddInformations__ = [i.name for i in AliOrdersAddInformation._meta.get_fields()]
        self.__fieldsAliOrdersProductList__ = [i.name for i in AliOrdersProductList._meta.get_fields()]
        # , AliOrdersProductList, AliGroupList, AliChildGroupList, AliOrdersAddInformation
        # self.buyer_info=data['buyer_info']
        # self.gmt_modified=data['gmt_modified']
        # self.gmt_create=data['gmt_create']
        # self.receipt_address=data['receipt_address']
        # self.logistic_info_list=data['logistic_info_list']
        # self.order_status=data['order_status']
        # self.payment_type=data.get('payment_type')
        # self.fund_status=data['fund_status']
        self.FIO=self.aliorderdetailed.FIO()
        # self.receipt_address=eval(self.aliorderdetailed.receipt_address)
        # self.phoneNumber=self.receipt_address['phone_country']+self.receipt_address['mobile_no']
        self.shipping_city=self.aliorderdetailed.shipping_city()
        self.shipping_index=self.aliorderdetailed.shipping_index()
        # self.shipping_index=self.receipt_address['zip']
        # self.pochta_normalize_adress=self.__pochta_normalize_adress__()
        # self.coord=self.__coords__()
        # self.products=data['global_aeop_tp_order_product_info_dto']


    # обновление данных из таблицы кастомных данных
    def __getAliDetailInfoOrder__(self):
            result=self.aliAPIsession.aliOrderInfo(self.order_id)['aliexpress_solution_order_info_get_response']['result']['data']
            inBD={item:result[item] for item in result if item in self.__fieldsAliOrdersAddInformations__}
            return inBD


    @property
    def pochta_normalised_adress(self):
        a = PochtaApi(client_id=loginPochta, client_secret=secretPochta, token=tokenPochta)
        m=['index', 'region', 'area', 'place', 'location','street', 'house',  'letter', 'corpus','building' ]
        addr = ','.join(list(map(lambda x: self.pochta_normalize_adress.get(x,''),m)))
        return a.normAddress(addr)


    def __getattr__(self, item):
        def evalHandler(s):
            if type(s) is str:
                if s[0]=='{':
                    s=eval(s)
            return s
        service, *rest=item.split('_') # service - имя сервиса в аттрибуте
        attr=rest.join('_') # attr - сам аттрибут
        print(f' сервис: {service}, аттрибут: {attr}')


        if item in self.__fieldsAliOrders__:
            return AliOrders.objects.get(order_id=self.order_id).__getattribute__(item)
        else:
            if item in self.__fieldsAliOrdersAddInformations__: # если искомый атрибут есть в таблице доп сведений
                res=self.aliorderdetailed.__getattribute__(item) #находим его значение
                if res: # если оно не пустое
                    return evalHandler(res) #возвращаем
                else:
                    data=self.__getAliDetailInfoOrder__() # получаем из AliAPI в словарь данные по таблице AliOrdersAddInformation
                    # data['pochta_normalize_adress'] = self.__pochta_normalize_adress__()
                    data['coord'] = self.__coords__()
                    AliOrdersAddInformation.objects.update_or_create(order=self.order_id, defaults=data)
                    return evalHandler(data[item])
            else:
                if item in self.__fieldsAliOrdersProductList__:
                    return AliOrdersProductList.objects.get(main_order=self.order_id).__getattribute__(item)
                else:
                    raise AttributeError(item)



    # def __getCdekTarifes__(self, toPostCode):
    #     CITIES_FROM = {'fromKazan': '420066', 'fromSaratov': '410012', 'fromChelny': '423802'}
    #     res = {item: Calc_tarif(from_post_code=CITIES_FROM[item],
    #                             to_post_code='121000').get_tarif() for item in CITIES_FROM}
    #     # fromKazan=Calc_tarif(from_post_code='420066', to_post_code=self.shipping_index).get_tarif()
    #     # fromSaratov = Calc_tarif(from_post_code='410012', to_post_code=self.shipping_index)
    #     # fromChelny= Calc_tarif(from_post_code='423802', to_post_code=self.shipping_index)
    #     self.cdek_tarifes=res


    # @property
    # def cdek_pvz(self):
    #     def calc_dist(inp): # расчёт дистанции от адреса получателя до СДЭК
    #         ax=float(self.coord['longitude'])
    #         bx=float(inp['location']['longitude'])
    #         ay=float(self.coord['latitude'])
    #         by=float(inp['location']['latitude'])
    #         return ((ax-bx)**2+(ay-by)**2)**(1/2)
    #     a=CdekAPI(client_id=Account, client_secret=Secure_password)
    #     listOfPVZ=a.GET_PVZ(postal_code=self.receipt_address['zip'])
    #     listOfPVZ.sort(key=calc_dist) # сортируем по дистанции до адреса получателя
    #     return listOfPVZ


    # def __pochta_normalize_adress__(self):
    #     a = PochtaApi(client_id=loginPochta, client_secret=secretPochta, token=tokenPochta)
    #     m=['zip', 'city', 'detail_address', 'address', 'address2']
    #     addr=','.join(list(map(lambda x: self.receipt_address.get(x,''),m)))
    #     return a.normAddress(addr)



    def product_list(self, insurance):
        products=AliOrdersProductList.objects.filter(main_order=self.order_id)
        weight=int(100/products.count())
        cost=int(int(insurance)/products.count())
        res=[{'name': 'Часы Восток', 'ware_key': re.search('\d{6}', item.product_name)[0],
              'payment': {'value': 0},'cost': cost, 'weight': weight, 'amount': 1} for item in products]
        return [{'number': '001', 'weight': 100, 'items': res }]


    def __coords__(self):
        addr=self.full_normalised_adress
        a=Geocoder(address=addr)
        return a.get_coords_by_address

    @check_funcs
    def calc_tarifes(self):
        fromKazan=Calc_tarif(from_post_code='420066', to_post_code=self.shipping_index)
        fromSaratov = Calc_tarif(from_post_code='410012', to_post_code=self.shipping_index)
        fromChelny= Calc_tarif(from_post_code='423802', to_post_code=self.shipping_index)
        return {'selectTarifKazan':fromKazan.get_tarif(), 'selectTarifSaratov':fromSaratov.get_tarif(), 'selectTarifChelny':fromChelny.get_tarif() }


class serviceAli():
    def __init__(self):
        self.session = AliApi(app_key=appAliKey, secret=Alisecret, sessionkey=AlisSessionKey)

    def __StrToDate__(self, dict, strTime, delta):
        for i in strTime:
            t=dict.get(i)
            if t:
                dt=datetime.strptime(f'{t} {delta}', '%Y-%m-%d %H:%M:%S %z')
                dict[i]=dt
        return dict

    def __SimpleMoneyToMoneyField__(self, dict, simpleMoney):
        for i in simpleMoney:
            s=dict.get(i)
            if s:
                dict[i]=Money(float(s['amount']), s['currency_code'])
        return dict

    @check_funcs
    def updateOrderList(self, depthUpdatingDays):
        a=iterOrderList(self.session.aliOrderList, depthUpdatingDays=depthUpdatingDays)
        print(len(a))
        j=0
        for i in a:
            j+=1
            print(j, ' ' , i)
            t=('gmt_update', 'gmt_send_goods_time', 'gmt_pay_time','gmt_create')
            m=('pay_amount', 'loan_amount', 'escrow_fee')
            i = self.__StrToDate__(i,t, '-0700')
            i=self.__SimpleMoneyToMoneyField__(i,m)
            productlist=i.pop('product_list')
            AliOrders.objects.update_or_create(order_id=i['order_id'], defaults=i)
            self.__importProductsInOrderList__(productlist['order_product_dto'], i['order_id'])

    def __importProductsInOrderList__(self, data, main_order_id):
        for i in data:
            t=('send_goods_time',)
            m=('total_product_amount', 'product_unit_price', 'logistics_amount')
            i = self.__StrToDate__(i,t, '+0800')
            i = self.__SimpleMoneyToMoneyField__(i,m)
            productID=i['product_id']
            i['product']=AliProducts.objects.get(product_id=productID)
            i['main_order']=AliOrders.objects.get(order_id=main_order_id)
            AliOrdersProductList.objects.update_or_create(order_id=i['order_id'], defaults=i)

    def updateProducts(self, depthUpdatingDays):
        a=iterProductList(self.session.aliProductList, depthUpdatingDays=depthUpdatingDays)
        print(len(a))
        j=0
        for i in a:
            j+=1
            print(j, ' ' , i)
            t=('gmt_create','gmt_modified')
            i = self.__StrToDate__(i,t,'+0800')
            AliProducts.objects.update_or_create(product_id=i['product_id'], defaults=i)


    def getProduct(self, id):
        return self.session.aliProductInfo(id)['aliexpress_solution_product_info_get_response']['result']

    def __getAliDetailInfoOrder__(self,id):
            FIELDS={'buyer_info', 'gmt_modified', 'receipt_address', 'gmt_trade_end', 'buyerloginid', 'order_status'}
            result=self.session.aliOrderInfo(id)['aliexpress_solution_order_info_get_response']['result']['data']
            inBD={item:result[item] for item in result if item in FIELDS}
            return inBD

    def __getCdekInfo__(self):
        CITIES_FROM={'fromKazan':'420066', 'fromSaratov': '410012', 'fromChelny':'423802'}
        res={item: Calc_tarif(from_post_code=CITIES_FROM[item],
                              to_post_code='121000').get_tarif() for item in CITIES_FROM}
        # fromKazan=Calc_tarif(from_post_code='420066', to_post_code=self.shipping_index).get_tarif()
        # fromSaratov = Calc_tarif(from_post_code='410012', to_post_code=self.shipping_index)
        # fromChelny= Calc_tarif(from_post_code='423802', to_post_code=self.shipping_index)
        return res
            # {'selectTarifKazan':fromKazan.get_tarif(), 'selectTarifSaratov':fromSaratov.get_tarif(), 'selectTarifChelny':fromChelny.get_tarif() }



    @check_funcs
    def getOrder(self, id):



        order = AliOrders.objects.get(order_id=id)
        orderInfo=AliOrdersAddInformation.objects.get_or_create(order=order, defaults=self.__getAliDetailInfoOrder__(id))[0]
        # if not AliOrdersAddInformation.objects.get(order=order):
        #     FIELDS={'buyer_info', 'gmt_modified', 'receipt_address', 'gmt_trade_end', 'buyerloginid', 'order_status'}
        #     result=self.session.aliOrderInfo(id)['aliexpress_solution_order_info_get_response']['result']['data']
        #     inBD={item:result[item] for item in result if item in FIELDS }
        #     AliOrdersAddInformation.objects.update_or_create(order=order, defaults=inBD)
        # orderInfo=AliOrdersAddInformation.objects.get(order=order)
        return orderInfo

    def __updateChildGroupList__(self, data, group_id):
        for i in data:
            i['ali_group']=AliGroupList.objects.get(group_id=group_id)
            AliChildGroupList.objects.update_or_create(group_id=i['group_id'], defaults=i)

    def updateGroupList(self):
        a=iterGroupList(self.session.aliGetGroupList)
        for i in a:
            print(i)
            if i.get('child_group_list'):
                child_group_list = i.pop('child_group_list')
                i['hasChild']=True
                AliGroupList.objects.update_or_create(group_id=i['group_id'], defaults=i)
                self.__updateChildGroupList__(child_group_list['aeop_ae_product_child_group'], i['group_id'])
            else:
                AliGroupList.objects.update_or_create(group_id=i['group_id'], defaults=i)




