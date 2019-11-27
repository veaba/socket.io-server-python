const net = require('net')
const host='127.0.0.1'
const port=233

const client = new net.Socket()
client.setEncoding('binary')


client.connect(port,host,()=>{
    client.write('aa?')
})

client.on('data',(data)=>{
    console.log(data)
    client.write('11')
})

client.on('error',err=>{
    client.destroy()
    throw err
})

client.on('close',()=>{
    console.log('close')
})