Object.assign(window, {
  textMesends:textMesends,
  conect:conect,
  NFTnokunka:NFTnokunka,
  start:start,
})

// window.global = window;
// window.Buffer = window.Buffer || require('buffer').Buffer;
// window.process = BrowserFS.BFSRequire('process');
// window.Buffer = BrowserFS.BFSRequire('buffer').Buffer;

const url:string = "";
const urlGeim:string = "";
const urlNFTbui:string = "";

function textMesends(moneu, distansion) {
  return "fff" + moneu + " " + distansion;
}

function start(url1,url2,url3){
  global.url = url1;
  global.urlGeim = url2;
  global.urlNFTbui = url3;
}



/////////////////////
// import {
//   Connection,
//   PublicKey,
//   Transaction,
//   clusterApiUrl,
//   SystemProgram,
//   Keypair,
//   LAMPORTS_PER_SOL,
// } from "@solana/web3.js";
import {tranzacsion,getProvider} from "./tranzact"
import {getData} from "./conect"



// const network = clusterApiUrl("mainnet-beta");
// const network = clusterApiUrl("testnet");



async function dd() {
  
}







async function conect() {
  try {
    const provaider = await getProvider();
    await provaider.connect();
    const p = provaider.publicKey.toString();
    await getData("POST", url, {
      id: p,
    });
    window.location.href = urlGeim;
  } catch (err) {
    window.open("https://phantom.app/", "_blank");
  }
}

// const getWalletBalance = async() => {
//   try{
//       const connection = new Connection(clusterApiUrl('devnet'),'confirmed')
//       const walletBalance = await connection.getBalance(publicKey)
//       console.log(`Wallet Balance is ${walletBalance}`)
//   }
//   catch(er){
//       console.log(er)
//   }
// }



async function NFTnokunka(i, y) {
  tranzacsion();

  // console.log(i);
  // await getData("POST", urlNFTbui, {
  //   NFT: i,
  //   onerasia: y,
  // });
  // window.location.href = "";
}


