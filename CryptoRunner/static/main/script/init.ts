import { tranzacsion, getProvider, getProviderConect } from "./tranzact";
import { getData, log } from "./funcsionLogic";
// import { run } from "./nft";
import {SmenaSilki} from "./js"

Object.assign(window, {
  textMesends: textMesends,
  conect: conect,
  NFTnokunka: NFTnokunka,
  start: start,
  BoxSunduk:BoxSunduk,
  buiNft:buiNft,
});

let url: string = "";
let urlGeim: string = "";
let urlNFT: string = "";
let domen: string = "";

function start(url1, url2, url3, url4) {
  url = url1;
  urlGeim = url2;
  urlNFT = url3;
  domen = url4;
}

function textMesends(moneu, distansion) {
  return (
    "In this Time, I ran " +
    distansion +
    " meters and Earn " +
    moneu +
    " Bonny Coin, in Bonny Game - Crypto Runner!\n" +
    "Let's Play, Earn and Trade Rewards With Me!\n" +
    domen +
    urlGeim
  );
}
////////

async function conect() {
  try {
    const provaider = await getProviderConect();
    const publicKey = provaider.publicKey.toString();
    await getData("POST", url, {
      publicKey: publicKey,
    });
    window.location.href = urlGeim;
  } catch (err) {
    window.open("https://phantom.app/", "_blank");
  }
}

async function NFTnokunka(i, y) {
  log(y);
  log(i);
  
  let signature = null;
  if (y == "bui") {
    document.getElementById("bloc1").style.display = "none";
    document.getElementById("bloc2").style.display = "";
    // document.getElementById("bloc2").textContent;

    signature = await tranzacsion();
    log(signature);
    if (!signature["signature"]) {
      log(signature["signature"]);
      window.location.href = "";
      return;
    }
    
    document.getElementById("bloc2").style.display = "none";
    document.getElementById("bloc3").style.display = "";

    await getData("POST", "", {
      NFT: i,
      onerasia: y,
      signatura: signature["signature"],
      conect: signature["NETWORK"],
    });
    return;
  }

  if (y == "sell") {
    let prises:any = await prompt("prais: snimaim 4%");
    prises = prises.replace(/,/g, ".");

    prises = parseFloat(prises);
    log(prises);
    log(isNaN(prises));
    if (isNaN(prises)) {
      alert("nou number");
      return;
    } else if (prises < 0.00001) {
      alert("malenkoe");
      return;
    }
    await getData("POST", "", {
      NFT: i,
      onerasia: y,
      prise: prises,
    });
    window.location.href = "";
    return;
  }

  await getData("POST", "", {
    NFT: i,
    onerasia: y,
  });
  window.location.href = "";
}


async function BoxSunduk(i) {
  log(i);

  document.getElementById("bloc1").style.display = "none";
  document.getElementById("bloc2").style.display = "";
  

  let signature = await tranzacsion();
  log(signature);
  if (!(signature["signaturess"])) {
    log(signature["signaturess"]);
    log(!signature["signaturess"]);
    window.location.href = "";
    return;
  }

  document.getElementById("bloc2").style.display = "none";
  document.getElementById("bloc3").style.display = "";
  SmenaSilki("","");


  let otvet = await getData("POST", "", {
    NFT: i,
    onerasia: "bui",
    signatura: signature["signaturess"],
    conect: signature["NETWORK"],
  });
  console.log(otvet);
  console.log(otvet["Eroor"]);
  return;
}

async function buiNft(i) {
  log(i);

  let signature = await tranzacsion(1);
  log(signature);
  if (!(signature["signaturess"])) {
    log(signature["signaturess"]);
    log(!signature["signaturess"]);
    window.location.href = "";
    return true;
  }

  let otvet = await getData("POSTBUI", "/DATA/", {
    signatura: signature["signaturess"],
    conect: signature["NETWORK"],
  });
  console.log(otvet);
  console.log(otvet["Eroor"]);
  return otvet["Eroor"];
}

