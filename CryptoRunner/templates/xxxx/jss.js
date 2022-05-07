let p;
async function conect() {
    try {
        const resp = await window.solana.connect();
        p = resp.publicKey.toString();
        console.log(p);
        return p;
    } catch (err) {
        window.open("https://phantom.app/", "_blank");
    }
}

async function conect2() {
    const res = await conect();
    window.location.href = "{% url 'profil'%}";
}

async function conect3() {
    const res = await conect();
    document.write(res);
}

async function conect4() {
    const solanaWeb3 = require('@solana/web3.js');
    console.log(solanaWeb3);
}







//