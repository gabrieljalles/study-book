import Button from './Button'

function Evento({numero}) {
    function meuEvento(){
        console.log(`FUI ATIVADO PELO MODO TURBO ${numero} ! `)
    }

    return(
        <div>
            <p>Clique para disparar um evento</p>
            <Button event={meuEvento} text="Primeiro evento"/>
        </div>
    )
}

export default Evento