const ORIGIN = location.origin
const HOST = window.location.protocol + "//" + window.location.host;

let headers = {}
const axi = axios.create({
    baseURL: HOST,
    headers: headers
});
