function test() {
    var p1 = document.getElementById('password1').value
    var p2 = document.getElementById('password2').value

    if(p1.length < 8) {
        alert('The password must be at least 8 digits.')
        return false
    }

    if(p1 != p2){
        alert('The password is different!!!')
        return false
    }
    else {
        alert('Passwords match.')
        return true
    }
}
