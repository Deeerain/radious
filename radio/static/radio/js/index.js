import Player from "./player/player.js"

const togglers = document.querySelectorAll('.toggler')
const favorite_buttons = document.querySelectorAll('#AddFavoriteButton')

try{
    const rp = new Player(document.querySelector('#RadioPlayer'))
        .init()
}
catch (Error) {
    console.error(Error)
}

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
        fetch(`/radio/${e.target.getAttribute('data-id')}/tofavorite/`, {
            method: 'post',
        }).then(r => {
            if (r.status == 200) {
                console.log("ok")
            }
        }).catch(e => {
            console.log(e)
        })
    })
}
