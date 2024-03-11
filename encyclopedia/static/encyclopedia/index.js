let labelEl = document.querySelector(".active");
let textEl = document.querySelector(".textar");
let input1 = document.querySelector(".input1");
const label1 = document.querySelector(".label1")


input1.addEventListener('focus',function(){
        label1.classList.add("activecl")

})

input1.addEventListener('blur',function(){
    if(input1.value === ""){
        label1.classList.remove("activecl")
    }
})

textEl.addEventListener('focus',function () {
        labelEl.classList.add('activecl')

})
textEl.addEventListener('blur',function () {
    if(textEl.value === ""){
        labelEl.classList.remove('activecl')
    }
})


