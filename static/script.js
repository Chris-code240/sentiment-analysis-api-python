



let form = document.getElementById('form')
form.addEventListener('submit',(ev)=>{
    ev.preventDefault()
    document.getElementById('result') ? document.getElementById('result').remove() : console.log("som text")
    const text = document.getElementById('text').value
    fetch('/endpoint',{
        method:'post',
        headers:{"Content-type":"application/json"},
        body:JSON.stringify({"data":text})
    }).then((res)=>{return res.json()}).then((jsonRes)=>{
        let p = document.createElement('p')
        p.setAttribute('id','result')
        const body = document.querySelector('body')
        p.textContent = `${jsonRes['message']}`
        body.appendChild(p)
    })

})