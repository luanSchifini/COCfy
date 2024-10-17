const data = '{{qs_json}}'
console.log(data)

const rdata = JSON.parse(data.replace(/&quot;/g, '""'))
console.log(data)

const input = document.getElementsById('search_here')
console.log(input)

let filteredArr = []

input.addEventListener('keyup', (e)=>{
    box.innerHTML = ""
    filteredArr = rdata.filter(info=> info['name'].includes(e.target.value))
    console.log(filteredArr)
    if (filteredArr.length > 0) {
        filteredArr.map(info=>{
            box.innerHTML += `<b>${info['name']}</b><br>`
        })
    } else {
        box.innerHTML = "<b>No results found...</b>"
    }
})