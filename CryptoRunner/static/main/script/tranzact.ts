import {
  Connection,
  PublicKey,
  Transaction,
  clusterApiUrl,
  SystemProgram,
  LAMPORTS_PER_SOL
} from "@solana/web3.js";
window.Buffer = window.Buffer || require('buffer').Buffer;

type DisplayEncoding = "utf8" | "hex";
type PhantomEvent = "disconnect" | "connect" | "accountChanged";
type PhantomRequestMethod =
  | "connect"
  | "disconnect"
  | "signTransaction"
  | "signAllTransactions"
  | "signMessage";

interface ConnectOpts {
  onlyIfTrusted: boolean;
}

interface PhantomProvider {
  publicKey: PublicKey | null;
  isConnected: boolean | null;
  signTransaction: (transaction: Transaction) => Promise<Transaction>;
  signAllTransactions: (transactions: Transaction[]) => Promise<Transaction[]>;
  signMessage: (
    message: Uint8Array | string,
    display?: DisplayEncoding
  ) => Promise<any>;
  connect: (opts?: Partial<ConnectOpts>) => Promise<{ publicKey: PublicKey }>;
  disconnect: () => Promise<void>;
  on: (event: PhantomEvent, handler: (args: any) => void) => void;
  request: (method: PhantomRequestMethod, params: any) => Promise<unknown>;
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

const NETWORK = clusterApiUrl("testnet");

export async function tranzacsion() {
  const conect = async () => {
    try {
      await provider.connect();
    } catch (err) {
      console.warn(err);
    }
  };


  const provider = getProvider();
  const connection = new Connection(NETWORK);
  // console.log(provider.publicKey);
  if(!provider.publicKey)await conect();
  if (!provider) return;

  const createTransferTransaction = async () => {
    // console.log(provider.publicKey);
    if (!provider.publicKey) return;
    let transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: provider.publicKey,
        toPubkey: provider.publicKey,
        lamports: 100,
      })
    );
    transaction.feePayer = provider.publicKey;
    const anyTransaction: any = transaction;
    anyTransaction.recentBlockhash = (
      await connection.getRecentBlockhash()
    ).blockhash;
    return transaction;
  };
  const sendTransaction = async () => {
    try {
      const transaction = await createTransferTransaction();
      if (!transaction) return;
      let signed = await provider.signTransaction(transaction);
      let signature = await connection.sendRawTransaction(signed.serialize());
      await connection.confirmTransaction(signature);
    } catch (err) {
      console.warn(err);
    }
  };
  const signMultipleTransactions = async (onlyFirst: boolean = false) => {
    try {
      const [transaction1, transaction2] = await Promise.all([
        createTransferTransaction(),
        createTransferTransaction(),
      ]);
      if (transaction1 && transaction2) {
        let txns;
        if (onlyFirst) {
          txns = await provider.signAllTransactions([transaction1]);
        } else {
          txns = await provider.signAllTransactions([
            transaction1,
            transaction2,
          ]);
        }
      }
    } catch (err) {
      console.warn(err);
    }
  };
  const signMessage = async (message: string) => {
    try {
      const data = new TextEncoder().encode(message);
      const res = await provider.signMessage(data);
    } catch (err) {
      console.warn(err);
    }
  };

  // console.log("start");
  await sendTransaction();
  await signMultipleTransactions();
}
