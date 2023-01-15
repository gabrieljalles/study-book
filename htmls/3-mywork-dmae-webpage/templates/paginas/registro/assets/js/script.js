class Validator{

    constructor(){
        this.validations = [
            'minLength',
            'maxLength',
            'onlyLetters',
            'hRequired',
            'emailValidate',
            'equal',
            'passwordValidate',
        ]
    }

    validate(form){
        //limpando validacoes antigas
        let currentValidations = document.querySelectorAll('form .error-validation');
        if(currentValidations.length){
            this.cleanValidations(currentValidations);
        }
        

        //pega todos os inputs
        let inputs = form.getElementsByTagName('input');
        let inputsArray = [...inputs];

        inputsArray.forEach(function(input, obj){
            for(let i =0; this.validations.length > i; i++){
                if(input.getAttribute(this.validations[i]) != null){
                    
                    let method = this.validations[i]
                    let value = input.getAttribute(this.validations[i]);
                    this[method](input,value);
                }
            }

        }, this);
    }

    //validação minimo de caracteres genêrico;
    minLength(input,minValue){
        let inputLength = input.value.length;
        let errorMessage = `O campo precisa ter ${minValue} caracteres!`;
        
        if(inputLength <minValue){
            this.printMessage(input, errorMessage);
        }
    }

    maxLength(input,maxValue){
        let inputLength = input.value.length;
        let errorMessage = `O campo permite até ${maxValue} caracteres!`;

        if(inputLength > maxValue){
            this.printMessage(input, errorMessage);
        }
    }

    //Apenas letras
    onlyLetters(input){
        let re = /^[A-Za-z]+$/;
        let inputValue = input.value;
        let errorMessage = `Este campo só permite Letras!`;
        if(!re.test(inputValue)){
            this.printMessage(input, errorMessage);
        }
    }

    emailValidate(input){
        let re= /\S+@\S+\.\S+/;
        let email = input.value;
        let errorMessage = `Insira um e-mail no formato jalles@seilaoque.com!`;

        if(!re.test(email)){
            this.printMessage(input,errorMessage);
        }
    }

    // verificar se um campo é igual a outro
    equal(input, inputName){
        let inputToCompare = document.getElementsByName(inputName)[0];
        let errorMessage = `Este campo precisa estar igual ao ${inputName}`;
        
        if(input.value != inputToCompare.value){
            this.printMessage(input, errorMessage);
        }
    }

    //torna o campo obrigatório
    hRequired(input){
        let inputValue =  input.value;

        if(inputValue === ''){
            let errorMessage = `Este campo é obrigatório!`;
            this.printMessage(input, errorMessage);
        }

    }

    //validador de senha
    passwordValidate(input){
       //
    }

    emailValidate(input){
        let re= /\S+@\S+\.\S+/;
        let email = input.value;
        let errorMessage = `Insira um e-mail no formato jalles@seilaoque.com!`;

        if(!re.test(email)){
            this.printMessage(input,errorMessage);
        }
    }

    // coloca a mensagem no html
    printMessage(input, msg){
        let errorsQtd = input.parentNode.querySelector('.error-validation');

        if(errorsQtd===null){
            let template = document.querySelector('.error-validation').cloneNode(true);
            template.textContent = msg;
            let inputParent = input.parentNode;
            template.classList.remove('template');
            inputParent.appendChild(template);
        }
    }

    //remove todas as validações
    cleanValidations(validations){
        validations.forEach(el => el.remove());
    }

}

//pegando elementos do HTML
const form = document.getElementById('formulario');
const submitBtn = document.getElementById('register');
const inputPass = document.getElementById('password');
const requirementsLength = document.getElementById('requirements-length');
const requirementsNumber = document.getElementById('requirements-numbers');
const requirementsLettersMa = document.getElementById('requirements-letters-ma');
const requirementsLettersMi = document.getElementById('requirements-letters-mi');
//chamando classe
let validator = new Validator();

//muda visual da senha entre verde e vermelho;
function changeVisualPass(password){
        let reNumber = /[0-9]/; 
        let reLetterMa = /[A-Z]/;
        let reLetterMi = /[a-z]/;
        requirementsLength.classList.remove('active-red','active-green');
        requirementsNumber.classList.remove('active-red','active-green');
        requirementsLettersMa.classList.remove('active-red','active-green');
        requirementsLettersMi.classList.remove('active-red','active-green');
        //tamanho
        if(password.length < 4 ){
            requirementsLength.classList.add('active-red');
        }else{
            requirementsLength.classList.remove('active-red');
            requirementsLength.classList.add('active-green');
        }

        //saber se possui número
        if(!reNumber.test(password)){
            requirementsNumber.classList.add('active-red');
        }else{
            requirementsNumber.classList.remove('active-red');
            requirementsNumber.classList.add('active-green');
        }

        //Conferir letras maiusculas
        if(!reLetterMa.test(password)){
            requirementsLettersMa.classList.add('active-red');
        }else{
            requirementsLettersMa.classList.remove('active-red');
            requirementsLettersMa.classList.add('active-green');
        }

        //Conferir letras minusculas
        if(!reLetterMi.test(password)){
            requirementsLettersMi.classList.add('active-red');
        }else{
            requirementsLettersMi.classList.remove('active-red');
            requirementsLettersMi.classList.add('active-green');
        }
    
}

// input escuta modificação
inputPass.addEventListener('input', (e)=>{
        let password = e.target.value;
        changeVisualPass(password);
});



//O botão executa classe;
submitBtn.addEventListener('click', function(e){
    e.preventDefault();
    validator.validate(form);
});
