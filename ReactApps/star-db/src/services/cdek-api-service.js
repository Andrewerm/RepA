class CdekApiService {
    _baseURL='https://api.cdek.ru/v2'
    _autorizationURL='/oauth/token'
    _session_Params= {}

    constructor(client_id, client_secret) {
        this.client_id = client_id;
        this.client_secret=client_secret
    }

    async get_token() {
        let urlencoded = new URLSearchParams();
        urlencoded.append('grant_type', 'client_credentials')
        urlencoded.append('client_id', this.client_id)
        urlencoded.append('client_secret', this.client_secret)

        const requestOptions = {
            method: 'post',
            headers: {
                "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            body: urlencoded,
            redirect: 'follow',
        };
        console.log(`urlencoded ${urlencoded}`);
        const res=await fetch(`${this._baseURL}${this._autorizationURL}`, requestOptions);
        this._session_Params=await res.json();
        console.log(` параметры 2 ${this._session_Params}`)


            // .then(response => {
            //     console.log(`response ${response}`)
            //     return response.json()})
            // .then(result => console.log(result))
            // .catch(error => console.log('error', error));



    }


}

export default CdekApiService

