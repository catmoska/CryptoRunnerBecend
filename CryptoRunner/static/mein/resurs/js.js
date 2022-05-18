Object.assign(window, {
  textMesends:textMesends,
  conect:conect,
  getData:getData,
  dd:dd,
  NFTnokunka:NFTnokunka,
})
window.global = window;
// @ts-ignore
window.Buffer = window.Buffer || require('buffer').Buffer;

function textMesends(moneu, distansion) {
  return "fff" + moneu + " " + distansion;
}

async function getData(method, url, body = null) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.responseType = "json";
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = () => {if (xhr.status >= 400) 
    reject(xhr.response);else resolve(xhr.response);};
    xhr.onerror = () => {reject(xhr.response);};
    xhr.send(JSON.stringify(body));
  });
}

/////////////////////
import {
  Connection,
  PublicKey,
  Transaction,
  clusterApiUrl,
  SystemProgram,
  Keypair,
  LAMPORTS_PER_SOL,
  publicKey,
} from "@solana/web3.js";
// import { debug } from "webpack";

// const resp = await window.solana.connect();
const anyWindow = window;
const provider = anyWindow.solana;
// const network = clusterApiUrl("mainnet-beta");Testnet
const network = clusterApiUrl("testnet");

// const createTransferTransaction = async () => {
//   console.log("dddddddddddddddddddddddd");
//   if (!window.solana.publicKey) {
//     console.log(window.solana.publicKey.toString());
//     console.log("fffffffffffffffff");
//     return;}
//   console.log("dddddddddddddddddddddddd");
//   let transaction = new Transaction().add(
//     SystemProgram.transfer({
//       fromPubkey: window.solana.publicKey,
//       toPubkey: window.solana.publicKey,
//       lamports: 100,
//     })
//   );
//   transaction.feePayer = window.solana.publicKey;
//   addLog("Getting recent blockhash");
//   const anyTransaction = transaction;
//   anyTransaction.recentBlockhash = (
//     await connection.getRecentBlockhash()
//   ).blockhash;
//   return transaction;
// };

// const sendTransaction = async () => {
//   try {
//     const transaction = await createTransferTransaction();
//     if (!transaction) return;

//     let signed = await window.solana.signTransaction(transaction);
//     addLog("Got signature, submitting transaction");
//     let signature = await connection.sendRawTransaction(signed.serialize());
//     addLog("Submitted transaction " + signature + ", awaiting confirmation");
//     await connection.confirmTransaction(signature);
//     addLog("Transaction " + signature + " confirmed");
//   } catch (err) {
//     console.warn(err);
//     addLog("[error] sendTransaction: " + JSON.stringify(err));
//   }
// };


async function dd() {
  // sendTransaction();
  // const resp = await window.solana.connect();

  // const connection = new Connection(
  //   network,
  //   'confirmed',
  // );

  const connection = new Connection(network);

  console.log("1");
  const from = Keypair.generate();
  const airdropSignature = await connection.requestAirdrop(
    from.publicKey,
    100, // 10000000 Lamports in 1 SOL
  );
  
  console.log("2");
  await connection.confirmTransaction(airdropSignature);

  // Generate a new random public key
  const to = Keypair.generate();

  
  console.log("3");
  console.log(from.publicKey.toString());
  console.log(to.publicKey.toString());
 

  const SPner= SystemProgram.transfer({
    fromPubkey: from.publicKey,
    toPubkey: to.publicKey,
    lamports: 100,
  })
  
  console.log(SPner);

  const transaction = new Transaction()
  .add(
    SPner,
  );

  const transaction2= new Transaction()
  .add(
    SystemProgram.transfer({
      fromPubkey: resp.publicKey,
      toPubkey: resp.publicKey,
      lamports: 100,
    })
  );


  // console.log(transaction);
  // const signedTransaction = await window.solana.signAndSendTransaction(transaction);


  // const {signature} = await window.solana.signAndSendTransaction(transaction);
  // await connection.confirmTransaction(signature);
}

















async function conect() {
  try {
    const resp = await window.solana.connect();
    const p = resp.publicKey.toString();
    console.log(resp.publicKey);
    console.log(resp.publicKey.toString());
    await getData("POST", url, {
      id: p,
    });
    // window.location.href = urlGeim;
  } catch (err) {
    // window.open("https://phantom.app/", "_blank");
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
  // dd();



  getWalletBalance()
  console.log(i);
  await getData("POST", urlNFTbui, {
    NFT: i,
    onerasia: y,
  });
  window.location.href = "";
}


