const player_element = document.querySelector('#RadioPlayer')
const radio_stream = new Audio(player_element.getAttribute('data-stream'))

const play_button = document.querySelector('#PlayControl')
const volume_changer = document.querySelector('#VolumeControl')
const pause_button = document.querySelector('#PauseControl')

pause_button.style.display = 'none'


volume_changer.value = radio_stream.volume


radio_stream.onplaying = (e) => {
    pause_button.style.display = 'block'
    play_button.style.display = 'none'
}

radio_stream.onpause = (e) => {
    pause_button.style.display = 'none'
    play_button.style.display = 'block'
}

volume_changer.addEventListener('input', (e) => {
    radio_stream.volume = volume_changer.value
})

pause_button.addEventListener('click', (e) => {
    radio_stream.pause()

})

play_button.addEventListener('click', (e) => {
    radio_stream.play()
})
