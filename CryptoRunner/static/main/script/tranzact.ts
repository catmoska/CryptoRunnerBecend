import {
  Connection,
  PublicKey,
  Transaction,
  clusterApiUrl,
  SystemProgram,
  Keypair,
  LAMPORTS_PER_SOL,
  
} from "@solana/web3.js";
import {
  getData,
  PhantomProvider,
  debug,
  taranzact,
  tanzacsiaRabota,
  log,
  EroorFhantom,
} from "./funcsionLogic";

let NETWORK: string;
if (debug) NETWORK = clusterApiUrl("testnet");
else NETWORK = clusterApiUrl("mainnet-beta");
let taranzactFuncia: (() => Promise<taranzact|null>)[] = [nftTaranzact];
const urlStatic: string = window.location.toString();

export async function tranzacsion(tin: number = 0) {
  
  const provider = await getProviderConect();
  const connection = new Connection(NETWORK);
  if (!provider) return false;
  
  let trnsPazm: taranzact|null;
  await taranzactFuncia[tin]().then(data => trnsPazm = data);
  if (trnsPazm == null)return false;
  log(trnsPazm);

  const createTransferTransaction = async () => {
    try {
    if (!provider.publicKey) return false;
    if (trnsPazm.publickeusol == null && trnsPazm.stoimost <= 0) return false;

    const publicKeyNrodaves = new PublicKey(trnsPazm.publickeusol);


    let transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: provider.publicKey,
        toPubkey: publicKeyNrodaves,
        lamports: LAMPORTS_PER_SOL * trnsPazm.stoimost,
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

  const sendTransaction = async () => {
    try {
      const transaction = await createTransferTransaction();
      if (!transaction) return false;
      let signed = await provider.signTransaction(transaction);
      log("Got signature, submitting transaction");
      let signature = await connection.sendRawTransaction(signed.serialize());
      log("Submitted transaction " + signature + ", awaiting confirmation");
      await connection.confirmTransaction(signature);
      log("Transaction " + signature + " confirmed");
      return signature;
    } catch (err) {
      console.warn(EroorFhantom(err["code"]));
      log("[error] sendTransaction: " + JSON.stringify(err));
      return false;
    }
  };

  log("start");
  const signature = await sendTransaction();
  log("fines");
  return {signature:signature,NETWORK:NETWORK}
}
/////////////////
export async function getWalletBalance() {
  try {
    const provider = await getProviderConect();
    const connection = new Connection(clusterApiUrl("devnet"), "confirmed");
    const walletBalance = await connection.getBalance(provider.publicKey);
    log(`Wallet Balance is ${walletBalance}`);
  } catch (er) {
    log(er);
  }
}

export function getProvider(): PhantomProvider | undefined {
  if ("solana" in window) {
    const anyWindow: any = window;
    const provider = anyWindow.solana;
    if (provider.isPhantom) {
      return provider;
    }
  }
  window.open("https://phantom.app/", "_blank");
}

export async function getProviderConect() {
  const provider = getProvider();
  try {
    try {
      await provider.connect({ onlyIfTrusted: true });
    } catch (err) {
      await provider.connect();
    }
  } catch (err) {
    console.warn(err);
  }
  return provider;
}

///////////////////////////

async function nftTaranzact(): Promise<taranzact|null> {
  let parameters:any = await getData("GETparams", "");
  if (parameters == "ErorEczemplar")
    return null;
  
  return {
    stoimost: parameters["stoimost"],
    publickeusol: "AtMCbPL5gjp2UdeZCki2c8FwXoY5fVfp3uAJ6hUDe4hw",
    // publickeusol:parameters["publickeusol"]
  };
}
