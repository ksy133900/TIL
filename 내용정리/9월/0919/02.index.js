const textInput = document.querySelector('#text-input')

textInput.addEventListener('input',function(event) {
  console.log(event)
  console.log(event.target.value)
})