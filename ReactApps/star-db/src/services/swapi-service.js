class SwapService {

    _apiBase = 'https://swapi.dev/api/';
    _imageBase='https://starwars-visualguide.com/assets/img/'

    async getSwapic(url1) {

        const res = await fetch(`${this._apiBase}${url1}`);
        if (!res.ok) {
            throw new Error(` не могу найти ${this._apiBase}${url1}`)
        }
        return await res.json()
    }

    getAllPeople=async ()=> {
        const res = await this.getSwapic('people/');
        return res.results.map(this._transformPerson)

    };

    getPerson=async (id)=> {
        const res = await this.getSwapic(`people/${id}/`);
        return this._transformPerson(res)
    };

    getPlanet=async (id)=> {
        const res = await this.getSwapic(`planets/${id}/`)
        return this._transformPlanet(res)
    }

    getPlanets=async()=> {
        const res = await this.getSwapic('planets/')
        return res.results.map(this._transformPlanet)
    }
    getStarships=async()=> {
        const res = await this.getSwapic('starships/')
        return res.results.map(this._transformStarship)
    }

    getStarship=async(id)=> {
        const res = await this.getSwapic(`starships/${id}`)
        return this._transformStarship(res)
    }


    getPersonImage=({id})=> {
         return `${this._imageBase}/characters/${id}.jpg`;
    };
    getStarshipImage=({id})=> {
        return `${this._imageBase}/starships/${id}.jpg`
    };
    getPlanetImage=({id})=> {
        return `${this._imageBase}/planets/${id}.jpg`
    };



    _extractId(item) {
        const idRegExp=/\/([0-9]*)\/$/;
        return item.url.match(idRegExp)[1];

    }
    _transformPlanet=(planet)=> {
        return {
                      id:this._extractId(planet),
                      name: planet.name,
                      populate: planet.population,
                      rotationPeriod: planet.rotation_period,
                      diameter: planet.diameter
                  }
    };

    _transformPerson=(person)=>{
        return {
            id:this._extractId(person),
            name: person.name,
            gender: person.gender,
            birthYear: person.birth_year,
            eyeColor: person.eye_color
        }
    }

    _transformStarship=(starship)=>{
        return {
            id:this._extractId(starship),
            name: starship.name,
            model: starship.model,
            manufacturer: starship.manufacturer,
            costInCredits: starship.costInCredits,
            length: starship.length,
            crew: starship.crew,
            passengers: starship.passengers,
            cargoCapacity: starship.cargoCapacity
        }
    }

}

export default SwapService





