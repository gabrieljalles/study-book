function OutraLista({itens}){
    return(
        <>
            <h3> Lista de coisas BOAS:</h3>
            {itens.length > 0 ? (
            itens.map((item, index)=>(
                <p key={index}>{item}</p>
            ))): "Os itens ainda não foram carregados ou passados"};
        </>
    )
}

export default OutraLista;