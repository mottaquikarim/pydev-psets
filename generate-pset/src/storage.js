export default class Storage {
    getItem(name, jsonify=false, default_="[]") {
        const data = localStorage.getItem(name)
        if (jsonify) {
            return JSON.parse(data || default_); 
        }

        return data;
    }

    setItem(name, val) {
        let valToSet = val;
        if (typeof val !== "string") {
            valToSet = JSON.stringify(val);
        }
        localStorage.setItem(name, valToSet);

        return  val;
    }

    removeItem(key) {
        localStorage.removeItem(key)
    }

    constructor() {
        this.token = this.getItem('token')
    }

    getStateModes() {
        return this.getItem('stateModes', true);
    }

    getPset() {
        return this.getItem('pset', true);
    }
}
