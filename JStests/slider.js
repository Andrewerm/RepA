
arr=['http://vostokinc.com/images/cms/thumbs/13556124a94737d154f84ee0029f092ccfc88d2f/amfibiya-060059_720_600_jpg_5_100.jpg',
    'http://vostokinc.com/images/cms/thumbs/5ae87a0a7c9086b055d8923267224c1ef88b06a2/amfibiya100315_720_600_png_5_100.png',
    'http://vostokinc.com/images/cms/thumbs/480157977f170d6b99be5d467ccf9544d874fff9/amfibiya-420007_720_600_png_5_100.png']
// let sl=slide(arr);



function CreateSlider() {
    return {
        imageURLS: [],
        position: 0,
        prevButton: null,
        nextButton: null,
        slideImage: null,
        nextBtnClick: function (e) {
            if (this.position===this.imageURLS.length-1) this.position=0;
            else this.position++;
            this.slideImage.src=this.imageURLS[this.position]},
        prevBtnClick: function (e) {
            if (this.position===0) this.position=this.imageURLS.length-1;
            else this.position--;
            this.slideImage.src=this.imageURLS[this.position]
        },
        start: function (id, arr) {
            let el=document.querySelector('div#itk-'+id+'.itk-slider')
            this.prevButton=el.querySelector('.prev-btn');
            this.nextButton=el.querySelector('.next-btn');
            this.slideImage=el.querySelector('img.img');
            this.imageURLS=arr;
            this.prevButton.addEventListener('click', this.prevBtnClick.bind(this));
            this.nextButton.addEventListener('click', this.nextBtnClick.bind(this))
    }
    };
    }


class CreateSlider1 {
    constructor () {
        this.imageURLS= [];
        this.position= 0;
        this.prevButton=null;
        this.nextButton=null;
        this.slideImage= null}
    nextBtnClick (e) {
            if (this.position===this.imageURLS.length-1) this.position=0;
            else this.position++;
            this.slideImage.src=this.imageURLS[this.position]}
    prevBtnClick (e){
            if (this.position===0) this.position=this.imageURLS.length-1;
            else this.position--;
            this.slideImage.src=this.imageURLS[this.position]
        }
    start (id, arr) {
            let el=document.querySelector('div#itk-'+id+'.itk-slider');
            this.prevButton=el.querySelector('.prev-btn');
            this.nextButton=el.querySelector('.next-btn');
            this.slideImage=el.querySelector('img.img');
            this.imageURLS=arr;
            this.prevButton.addEventListener('click', this.prevBtnClick.bind(this));
            this.nextButton.addEventListener('click', this.nextBtnClick.bind(this))
        }
    };





slider1=CreateSlider()
slider2=new CreateSlider()
slider3=new CreateSlider1()
slider4=new CreateSlider1()
slider1.start(1, arr)
slider2.start(2, arr)
slider3.start(3, arr)
slider4.start(4, arr)





