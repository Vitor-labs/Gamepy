import axios from "axios";

export function get_games() {
    return axios.get('http://127.0.0.1:8000/games/')
        .then(res => {
            return res.data
        })
}

export function add_game(game: object) {
    return axios.post('http://127.0.0.1:8000/games/',
        {
            patient_id: null,
            first_name: game.first_name.value,
            last_name: game.last_name.value,
            blood: game.blood.value,
        })
        .then(res => {
            return res.data
        })
}

export function edit_game(id: number, patient: object) {
    return axios.put('http://127.0.0.1:8000/patient/' + id + '/',
        {
            first_name: patient.first_name.value,
            last_name: patient.last_name.value,
            blood: patient.blood.value,
        })
        .then(res => {
            return res.data
        })
}

export function del_game(id) {
    return axios.delete('http://127.0.0.1:8000/game/' + id + '/')
        .then(res => {
            return res.data
        })
}
