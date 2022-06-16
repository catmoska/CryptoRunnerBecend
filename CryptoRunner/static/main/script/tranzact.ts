import {
  Connection,
  PublicKey,
  Transaction,
  clusterApiUrl,
  SystemProgram,
  // Keypair,
  LAMPORTS_PER_SOL,
} from "@solana/web3.js";
import {
  getData,
  PhantomProvider,
  debug,
  taranzact,
  // tanzacsiaRabota,
  log,
  // EroorFhantom,
  // signaturaX2
} from "./funcsionLogic";
// import {
//   getAccount,
//   createMint,
//   createAccount,
//   mintTo,
//   getOrCreateAssociatedTokenAccount,
//   transfer,
// } from "@solana/spl-token/module.flow";

// ?????????
const Nrosent: number = 0.04;                     // ?????????? ?????????
const publickeusolAvtor: string =
  "AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw"; // ???? ?????????? ????????
const stoimostOplati: number = 0.005;             // ????????? ?????? box unity

// ????????? ??? ??????????
let NETWORK: string;
if (debug) NETWORK = clusterApiUrl("testnet");
else NETWORK = clusterApiUrl("mainnet-beta");
let taranzactFuncia: (() => Promise<taranzact | null>)[] = [nftTaranzact,nftTaranzactMin];
const urlStatic: string = window.location.toString();


// ?????????? ???
export async function tranzacsion(tin: number = 0) {
  const provider = await getProviderConect();
  const connection = new Connection(NETWORK);
  if (!provider) return false;

  let trnsPazm: taranzact | null;
  await taranzactFuncia[tin]().then((data) => (trnsPazm = data));
  if (trnsPazm == null) return false;
  log(trnsPazm);

  // ???????? ??????????
  const createTransferTransaction = async (tin: boolean = false) => {
    try {
      if (!provider.publicKey) return false;
      if (trnsPazm.publickeusol == null && trnsPazm.stoimost <= 0) return false;

      let publickeusol = trnsPazm.publickeusol;
      let stoimost = trnsPazm.stoimost;
      if (tin) {
        publickeusol = publickeusolAvtor;
        stoimost = stoimost * Nrosent;     //????????
      } else {
        stoimost = stoimost * (1 - Nrosent);
      }

      const publicKeyNrodaves = new PublicKey(publickeusol);

      let transaction = new Transaction().add(
        SystemProgram.transfer({
          fromPubkey: provider.publicKey,
          toPubkey: publicKeyNrodaves,
          lamports: LAMPORTS_PER_SOL * stoimost,
        })
      );
      transaction.feePayer = provider.publicKey;
      log("Getting recent blockhash");
      const anyTransaction: any = transaction;
      anyTransaction.recentBlockhash = (
        await connection.getRecentBlockhash()
      ).blockhash;
      return transaction;
    } catch (err) {
      return false;
    }
  };
  

  // ?????? ? ?????????? ????? ?????????? 
  // const sendTransaction = async () => {
  //   try {
  //     const transaction = await createTransferTransaction();
  //     if (!transaction) return false;
  //     let signed = await provider.signTransaction(transaction);
  //     log("Got signature, submitting transaction");
  //     let signature = await connection.sendRawTransaction(signed.serialize());
  //     log("Submitted transaction " + signature + ", awaiting confirmation");
  //     await connection.confirmTransaction(signature);
  //     log("Transaction " + signature + " confirmed");
  //     return signature;
  //   } catch (err) {
  //     try {
  //       console.warn(EroorFhantom(err["code"]));
  //     } catch (err) {
  //       console.warn(err);
  //     }

  //     log("[error] sendTransaction: " + JSON.stringify(err));
  //     return false;
  //   }
  // };

  // ?????? ? ?????????? ???? ?????????? 
  const signMultipleTransactions = async () => {
    try {
      const [transaction1, transaction2] = await Promise.all([
        createTransferTransaction(true),
        createTransferTransaction(false),
      ]);
      if (transaction1 && transaction2) {
        let txns;
        txns = await provider.signAllTransactions([transaction1, transaction2]);

        log(txns);
        let signature1 = await connection.sendRawTransaction(
          txns[0].serialize()
        );
        let signature2 = await connection.sendRawTransaction(
          txns[1].serialize()
        );
        log("Submitted transaction " + signature1 + ", awaiting confirmation");
        log("Submitted transaction " + signature2 + ", awaiting confirmation");
        await connection.confirmTransaction(signature1);
        await connection.confirmTransaction(signature2);
        log("Transaction " + signature1 + " confirmed");
        log("Transaction " + signature2 + " confirmed");
        return { signature1, signature2 };
      }
    } catch (err) {
      console.warn(err);
      console.warn("dddd");
    }
  };

  log("start");
  const signaturess = await signMultipleTransactions(); //start
  log("fines");
  log(signaturess);
  return { signature:signaturess, NETWORK: NETWORK };
}


/////////////////
// // ?????? ??????
// export async function getWalletBalance() {
//   try {
//     const provider = await getProviderConect();
//     const connection = new Connection(clusterApiUrl("devnet"), "confirmed");
//     const walletBalance = await connection.getBalance(provider.publicKey);
//     log(`Wallet Balance is ${walletBalance}`);
//   } catch (er) {
//     log(er);
//   }
// }

// ?????? ?????????
export function getProvider(): PhantomProvider | undefined {
  if ("solana" in window) {
    const anyWindow: any = window;
    const provider = anyWindow.solana;
    if (provider.isPhantom) return provider;
    
    console.log("wwwwwwwwwwwwwwww");
    console.log(provider); 
    console.log(provider.isPhantom);
  }
  //window.open("https://phantom.app/", "_blank");
}


// ??????????? ? solana
export async function getProviderConect() {
  const provider = getProvider();
  console.log(provider);
  try {
    try {
      await provider.connect({ onlyIfTrusted: true });
    } catch (err) {
      await provider.connect();
    }
    return provider;
  } catch (err) {
    console.log("Error \n"+err);
    // return provider;
  }
}


///////////////////////////

// ?????????? ?? ??????? nft
async function nftTaranzact(): Promise<taranzact | null> {
  let parameters: any = await getData("GETparams", "");
  if (parameters == "ErorEczemplar") return null;

  return {
    stoimost: parameters["stoimost"],
    publickeusol: parameters["publickeusol"],
  };
}

// ?????????? ?? ??????? box unity
async function nftTaranzactMin(): Promise<taranzact | null> {
  return {
    stoimost: stoimostOplati,
    publickeusol: publickeusolAvtor,
  };
}

