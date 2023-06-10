import Player from "./player/player.js"

const togglers = document.querySelectorAll('.toggler')
const favorite_buttons = document.querySelectorAll('#AddFavoriteButton')

const rp = new Player(document.querySelector('#RadioPlayer'))
    .init()

const feedback_form = document.querySelector("#feedbackForm");

// feedback_form.addEventListener("submit", (ev) => {
//     ev.preventDefault()
    
//     const form_data = new FormData(ev.target)
//     const form_action = ev.target.getAttribute("action")
//     const form_method = ev.target.getAttribute("method")

//     fetch(form_action, {
//         method: form_method,
//         body: form_data
//     }).then(response => {
//         console.log(response)
//     }).catch(reason => {
//         console.error(reason)
//     })
// })

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