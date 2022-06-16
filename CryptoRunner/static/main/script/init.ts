// import
import { tranzacsion, getProvider, getProviderConect } from "./tranzact";
import { getData, log } from "./funcsionLogic";
// import { run } from "./nft";
import { SmenaSilki, SmenaBackground,displayStile } from "./js";

// Global function
Object.assign(window, {
  textMesends: textMesends,
  conect: conect,
  NFTnokunka: NFTnokunka,
  start: start,
  BoxSunduk: BoxSunduk,
  StartbuiNft: StartbuiNft,
  getData:getData,
  log:log,
});

// start peramenii
let url: string = "";
let urlGeim: string = "";
let urlNFT: string = "";
let domen: string = "";
let Referral: string = "";

function start(url1, url2, url3, url4,Referra) {
  url = url1;
  urlGeim = url2;
  urlNFT = url3;
  domen = url4;
  Referral =Referra;
}

// ??????? ????????? ????????
function textMesends(moneu, distansion) {
  return (
    "In this Time, I ran " +
    distansion +
    " meters and Earn " +
    moneu +
    " Bonny Coin, in Bonny Game - Crypto Runner!\n " +
    "Let's Play, Earn and Trade Rewards With Me!\n " +
    Referral
  );
}
////////
// ??????? ?????????????? ??????
async function conect() {
  try {
    console.log("start");
    const provaider = await getProviderConect();
    console.log(provaider);
    const publicKey = provaider.publicKey.toString();
    console.log(publicKey);
    await getData("POST", url, {
      publicKey: publicKey,
    });
    window.location.href = urlGeim;
  } catch (err) {
    console.log("fff");
    //window.open("https://phantom.app/", "_blank");
  }
}

//////////////////////////////////////////
// ?????? ??????? ? ?????? ? ???????
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
      log(signature);
      setTimeout(() => (window.location.href = ""), 1000);
      return;
    }

    document.getElementById("bloc2").style.display = "none";
    document.getElementById("bloc3").style.display = "";

    await getData("POST", "", {
      NFT: i,
      onerasia: y,
      signatura: signature,
    });
    return;
  }

  if (y == "sell") {
    let prises: any = await prompt("Now You Will Sell Your Bonny NFT. Plese Select The Price in Solana! We Take 4% as a Fee, If your NFT will be sold.");
    prises = prises.replace(/,/g, ".");

    prises = parseFloat(prises);
    log(prises);
    log(isNaN(prises));
    if (isNaN(prises)) {
      alert("Please, try Again! The Incorrect Number");
      return;
    } else if (prises < 0.00001) {
      alert("Please, try Again! The Incorrect Number");
      return;
    }
    await getData("POST", "", {
      NFT: i,
      onerasia: y,
      prise: prises,
    });
    await alert("Complete! Now Your NFT already On Marketplace!");
    setTimeout(() => (window.location.href = ""), 1000);
    return;
  }

  await getData("POST", "", {
    NFT: i,
    onerasia: y,
  });

  setTimeout(() => (window.location.href = ""), 1000);
}

/////////////////////
//??????? box
async function BoxSunduk(i) {
  log(i);

  document.getElementById("bloc1").style.display = "none";
  document.getElementById("bloc2").style.display = "";

  let signature = await tranzacsion();
  log(signature);
  if (!signature["signature"]) {
    log(signature["signature"]);
    log(!signature["signature"]);
    setTimeout(() => (window.location.href = ""), 500);
    return;
  }

  document.getElementById("bloc2").style.display = "none";
  document.getElementById("bloc3").style.display = "";
  SmenaSilki("", "");

  let otvet = await getData("POST", "", {
    NFT: i,
    onerasia: "bui",
    signatura: signature,
  });
  console.log(otvet);
  console.log(otvet["Eroor"]);
  return;
}

/////////////////////
//unity ?????????? ??? BoxSunduk
let i = false;
let d = false;

// ?????????????
function StartbuiNft(): boolean {
  log("StartbuiNft  " + i);
  if (i) return false;
  if (!i) {
    if (d) {
      d = false;
      log("dasdJS Finall");
      return true;
    }
    buiNft1();
    // log("dasdJS");
    return false;
  }
}

// ??????????
async function buiNft1() {
  i = true;
  await buiNft();
  i = false;
  d = true;
}

// ??????????
async function buiNft() {
  displayStile("bloc1",false,800);
  await displayStile("bloc2",true);

  let background = SmenaBackground("");

  let signature = await tranzacsion(1);
  log(signature);
  if (!signature["signature"]) {
    log(signature["signature"]);
    log(!signature["signature"]);
    setTimeout(() => (window.location.href = ""), 500);
    return true;
  }
  SmenaBackground(background);

  let otvet = await getData("POSTBUI", "/DATA/", {
    signatura: signature,
  });
  if (otvet["Eroor"]) {  
    log(otvet);
    setTimeout(() => (window.location.href = ""), 500);
    return true;
  }

  log(otvet);
  document.getElementById("bloc1").style.display = "";
  document.getElementById("bloc2").style.display = "none";
  return otvet["Eroor"];
}

/////////////////////
