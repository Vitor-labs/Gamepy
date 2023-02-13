import axios from "axios";

interface Game {
    id: number;
    name: string;
    price: number;
    score: number;
    publisher: string;
    pub_date: string;
    cover: File;
    summary: string;
    genre: string;
}

export function get_games() {
    return axios.get('http://127.0.0.1:8000/games/')
        .then(res => {
            return res.data
        })
}

export function add_game(game: Game) {
    return axios.post('http://127.0.0.1:8000/games/',
        {
            id: null,
            name: 'shadow of war',
            price: 230.55,
            score: 12,
            publisher: 'square_inix',
            pub_date: '12/02/2012',
            cover: 'some/path/to/url',
            summary: 'loren ipsum, lorem lorem ipsum ipsum',
            genre: 'ACT'
        })
        .then(res => {
            return res.data
        })
}

export function edit_game(id: number, game: Game) {
    return axios.put('http://127.0.0.1:8000/game/' + id + '/',
        {
            'id': game.id,
            'name': game.name,
            'price': game.price,
            'score': game.score,
            'publisher': game.publisher,
            'pub_date': game.pub_date,
            'cover': game.cover,
            'summary': game.summary,
            'genre': game.genre
        })
        .then(res => {
            return res.data
        })
}

export function del_game(id: number) {
    return axios.delete('http://127.0.0.1:8000/game/' + id + '/')
        .then(res => {
            return res.data
        })
}
