
var draw = function() {
  let res = JSON.parse(this.responseText)
  let swag = ''
  for(var n in res) {
    pixel = res[n]
    //ctx.fillStyle = pixel['color']
    //ctx.fillRect(pixel['x'], pixel['y'], 1,1)

    swag += `<rect width="1" height="1" style="fill:${res[n]['color']};stroke-width:1;stroke:rgb(0,0,0)" />`
  }
  document.getElementById('swag').innerHTML = swag
}

var reloadPikk = function() {
  var req = new XMLHttpRequest()
  req.addEventListener('load', draw)
  req.open('GET', '/swag')
  req.send()
}

reloadPikk()

/*

function draw() {
  console.log(this.responseText)
}

var req = new XMLHttpRequest()
req.addEventListener('load', draw)
req.open('GET', '/pikk')
req.send()

*/
