function Saudacao({nome}){

    function gerarSaudacao(algumNome){
        return `Olá, ${algumNome} SEJA MUITO BEM VINDO `
    }

    return (
        <>
            {nome &&
                <p>{(gerarSaudacao(nome))}</p>
            }
        </>
    )
}

export default Saudacao