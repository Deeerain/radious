class Player {
    radio_element
    src
    audio

    play_button
    volume_changer

    constructor (radio_element) {
        this.radio_element = radio_element
        this.src = this.radio_element.getAttribute('data-stream')
    }

    init() {
        this.radio_element.style.display = 'flex'
        this.radio_element.style.flexDirection = 'column'
        this.radio_element.style.alignItems = 'center'

        this.audio = new Audio(this.src)
        
        this.play_button = document.createElement('button')
        this.volume_changer = document.createElement('input')
        
        this.play_button.classList.add('player__play-button')
        this.play_button.classList.add('material-symbols-outlined')
        this.play_button.style.fontSize = '75px'
        this.play_button.innerText = 'play_circle'
        
        this.volume_changer.setAttribute('type', 'range')
        this.volume_changer.setAttribute('min', 0)
        this.volume_changer.setAttribute('max', 1)
        this.volume_changer.setAttribute('step', 0.1)
        
        this.radio_element.append(this.play_button)
        this.radio_element.append(this.volume_changer)
        
        this.play_button.addEventListener('click', (ev) => this.play_handler(ev, this))

        this.volume_changer.addEventListener('input', (ev) => this.change_volume_handler(ev, this))
        this.audio.addEventListener('play', (ev) => this.audo_on_playing(ev, this))
        this.audio.addEventListener('pause', (ev) => this.audio_on_paused(ev, this))
    }

    audo_on_playing(ev, player) {
        player.play_button.innerText = 'pause_circle'
    }

    audio_on_paused(ev, player) {
        player.play_button.innerText = 'play_circle'
    }

    play_handler(ev, player) {
        if (player.audio.paused) {
            player.audio.play()
            return
        }

        player.audio.pause()
    }

    change_volume_handler(ev, player) {
        player.audio.volume = ev.target.value
    }
}

export default Player