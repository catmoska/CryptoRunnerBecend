function textMesends(moneu, distansion) {
  return "fff" + moneu + " " + distansion;
}
async function conect() {
  const url = "{% url 'geim'%}";
  try {
    const resp = await window.solana.connect();
    p = resp.publicKey.toString();
    // console.log(p);
    await getData("POST", url, {
      id: p,
    });
    window.location.href = "{% url 'geim'%}";
  } catch (err) {
    window.open("https://phantom.app/", "_blank");
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
