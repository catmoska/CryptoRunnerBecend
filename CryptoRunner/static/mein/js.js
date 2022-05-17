// import {
//   Connection,
//   PublicKey,
//   Transaction,
//   clusterApiUrl,
//   SystemProgram,
// } from "https://unpkg.com/@solana/web3.js";


const network = clusterApiUrl("mainnet-beta");
// const connection = new Connection("mainnet-beta","confirmed");

while (true){
  let o = await sec(1000);
  sayHi()
}













function textMesends(moneu, distansion) {
  return "fff" + moneu + " " + distansion;
}

async function conect() {
  try {
    const resp = await window.solana.connect();
    p = resp.publicKey.toString();
    await getData("POST", url, {
      id: p,
    });
    window.location.href = urlGeim;
  } catch (err) {
    // window.open("https://phantom.app/", "_blank");
  }
}

async function getData(method, url, body = null) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();

    xhr.open(method, url);

    xhr.responseType = "json";
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = () => {
      if (xhr.status >= 400) reject(xhr.response);
      else resolve(xhr.response);
    };

    xhr.onerror = () => {
      reject(xhr.response);
    };

    xhr.send(JSON.stringify(body));
  });
}

async function dd() {
  const network = clusterApiUrl("mainnet-beta");
  
  const connection = new Connection(network);
  const transaction = new Transaction();
  const {signature} = await window.solana.signAndSendTransaction(transaction);
  await connection.confirmTransaction(signature);
}

const getWalletBalance = async() => {
  try{
      const connection = new Connection(clusterApiUrl('devnet'),'confirmed')
      const walletBalance = await connection.getBalance(publicKey)
      console.log(`Wallet Balance is ${walletBalance}`)
  }
  catch(er){
      console.log(er)
  }
}

async function NFTnokunka(i, y) {
  // getWalletBalance()
  dd();
  // console.log(i);
  await getData("POST", urlNFTbui, {
    NFT: i,
    onerasia: y,
  });
  // window.location.href = "";
}


