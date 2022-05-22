import { PublicKey, Transaction } from "@solana/web3.js";
import axios from "axios";
export const debug = true;
window.Buffer = window.Buffer || require("buffer").Buffer;

export async function getData(
  method: string,
  url: string,
  body: object = null
) {
  let res: object;
  await axios({
    method: method,
    url: url,
    data: body,
  }).then((deta) => (res = deta));

  let resy = res["data"];

  try {
    let obj:object = JSON.parse(JSON.stringify(resy));
    return obj;
  } catch (err) {
    return resy;
  }
}

export function log(text) {
  if (debug) console.log(text);
}

let eroor = 
{"4900":"Phantom could not connect to the network.", 
"4100":"The requested method and/or account has not been authorized by the user.", 
"4001":"The user rejected the request through Phantom.",
"-32000":"Missing or invalid parameters.", 
"-32003":"Phantom does not recognize a valid transaction.", 
"-32601":"Phantom does not recognize the method.", 
"-32603":"Something went wrong within Phantom."};
export function EroorFhantom(num):string{
  try{
  let res:string = eroor[num.toString()]
  }catch(err){}
  return num;
}









///////////////////////////////////////////////
export type DisplayEncoding = "utf8" | "hex";
export type PhantomEvent = "disconnect" | "connect" | "accountChanged";
export type PhantomRequestMethod =
  | "connect"
  | "disconnect"
  | "signTransaction"
  | "signAllTransactions"
  | "signMessage";

export interface ConnectOpts {
  onlyIfTrusted: boolean;
}

export interface PhantomProvider {
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

export interface taranzact {
  stoimost: number;
  publickeusol: string;
}

export interface tanzacsiaRabota {
  potvezenia: string | null;
  nrisina: string | null;
}
