export default class SwapiService {
    _apiBase = 'https://swapi.dev/api/';
    _urlBAse='https://starwars-visualguide.com/assets/img/'

    async getSwapi(url1) {
        const ur = this._apiBase + url1;
        const res=await fetch(ur)
        const res2=await res.json()
        return res2
    }

    getPlanetInfo=async(id)=> {
        const result2=await this.getSwapi(`planets/${id}/`)
        return this._transformPlanet(result2)
    }

    getPlanets=async ()=> {
        const result=await this.getSwapi(`planets/`);
        return result.results.map(i=>this._transformPlanet(i))
    }

    getPerson=async (id)=> {
        const res = await this.getSwapi(`people/${id}/`)
        return this._transformPerson(res)
    }

    getAllPeople=async ()=> {
        const result =await this.getSwapi('people/');
        return result.results.map(this._transformPerson)

    }

    getAllShips=async ()=>{
        const result =await this.getSwapi('starships/');
        return result.results.map(this._transformStarship)
    }

    getShip=async(id)=>{
        const res = await this.getSwapi(`starships/${id}/`);
        return this._transformStarship(res)
    }

    _extractId(i) {
        const idRegExp=/\/([0-9]*)\/$/;
        return i.match(idRegExp)[1]

    }

    _transformPlanet=(obj)=> {
        return {id: this._extractId(obj.url),
            name: obj.name,
            diameter: obj.diameter,
            populate:obj.population,
            rotationPeriod:obj.rotation_period}
    };

    _transformPerson=(person)=>{
        return {
            id:this._extractId(person.url),
            name: person.name,
            gender: person.gender,
            birthYear: person.birth_year,
            eyeColor: person.eye_color
        }
    };

    _transformStarship=(starship)=>{
        return {
            id:this._extractId(starship.url),
            name: starship.name,
            model: starship.model,
            manufacturer: starship.manufacturer,
            costInCredits: starship.costInCredits,
            length: starship.length,
            crew: starship.crew,
            passengers: starship.passengers,
            cargoCapacity: starship.cargoCapacity
        }
    };

    getPlanetImage=({id})=> {
        return `${this._urlBAse}/planets/${id}.jpg`
    };
    getPersonImage=({id})=> {
        return `${this._urlBAse}/characters/${id}.jpg`
    };
    getStarshipImage=({id})=> {
        return `${this._urlBAse}/starships/${id}.jpg`
    }



}

