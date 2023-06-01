import Player from "./player/player.js"

const togglers = document.querySelectorAll('.toggler')
const favorite_buttons = document.querySelectorAll('#AddFavoriteButton')

const rp = new Player(document.querySelector('#RadioPlayer'))
    .init()

for (let toggler of togglers) {
    toggler.addEventListener('click', (e) => {
        const toggle_target_query = e.target.getAttribute('data-target')
        const toggle_class_name = e.target.getAttribute('data-class-name')

        const toggle_target = document.querySelector(toggle_target_query)
        toggle_target.classList.toggle(toggle_class_name)
    }) 
}

for (let f_button of favorite_buttons) {
    f_button.addEventListener('click', (e) => {
        const id =  Number(e.target.getAttribute('data-id'))
        let favorites = JSON.parse(sessionStorage.getItem('favorites'))


        if (favorites == null){
            favorites = Array()
            favorites.push(id)
        } else if (favorites.includes(id)) {
            return
        }else {
            favorites.push(id)
        }

        sessionStorage.setItem('favorites', JSON.stringify(favorites))

        console.log(sessionStorage)
    })
}