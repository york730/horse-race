
// TODO: get response and render

const horses = {
  '1': [3, 4],
  '2': [1, 2, 6],
  '3': [3, 5, 6],
  '4': [4, 5],
  '5': [3, 4],
  '6': [2, 4, 6]
};

const requestBodyIndex = ["一號", "二號", "三號", "四號"]


function createHorseCompetitors() {

  const horseList = document.getElementById('horseList');

  for (let key in horses) {
    const div = document.createElement('div');
    div.classList.add('horse-item');
    div.innerHTML = `<label>${key}: </label><input type="text" class="input-field" id="input-${key}" value="${horses[key]}" />`;
    horseList.appendChild(div);
  }

}

function createPlayers() {
  const container = document.getElementById("raceList");

  for (let i = 1; i <= 4; i++) {
    // 創建外層 div
    const flexDiv = document.createElement("div");
    flexDiv.className = "flex";

    // 創建第1個 input 和 p 標籤
    const input1 = document.createElement("input");
    input1.type = "number";
    input1.min = 0;
    input1.max = 10;
    input1.id = `input-${i}-1`;
    const p = document.createElement("p");
    p.textContent = i;

    // 創建第一個 flex-stretch 包含的多個 input
    const stretchDiv1 = document.createElement("div");
    stretchDiv1.className = "flex flex-stretch";

    for (let j = 2; j <= 7; j++) {
      const input = document.createElement("input");
      input.type = "number";
      input.min = 0;
      input.max = 10;
      input.id = `input-${i}-${j}`; // 動態生成id
      stretchDiv1.appendChild(input);
    }

    // 創建第二個 flex-stretch 包含1個 input
    const stretchDiv2 = document.createElement("div");
    stretchDiv2.className = "flex flex-stretch";

    const input2 = document.createElement("input");
    input2.type = "number";
    input2.min = 0;
    input2.max = 10;
    input2.id = `input-${i}-8`; // 動態生成id
    stretchDiv2.appendChild(input2);

    // 將所有子元素加入外層 div: 賽道、出賽的馬匹、道具、押金
    flexDiv.appendChild(p);
    flexDiv.appendChild(input1);
    flexDiv.appendChild(stretchDiv1);
    flexDiv.appendChild(stretchDiv2);

    // 將外層 div 加入 container
    container.appendChild(flexDiv);
  }
}

  // 取得所有 input 值並組成 JSON
  function getInputValuesAsBody() {
    const userInputs = document.querySelectorAll("input[type='number']");
    const values = {};

    userInputs.forEach((input) => {
      values[input.id] = input.value || 0; // 如果輸入為空值，預設為0
    });
  
    const data = {};
    for (let i = 1; i <= 4; i++) {
      const horseValue = horses[values[`input-${i}-1`]];
      data[requestBodyIndex[i-1]] = [
                                  horseValue, 
                                  [
                                    +values[`input-${i}-2`],
                                    +values[`input-${i}-3`],
                                    +values[`input-${i}-4`],
                                    +values[`input-${i}-5`],
                                    +values[`input-${i}-6`],
                                    +values[`input-${i}-7`],
                                  ],
                                  +values[`input-${i}-8`]
                                ]
    }
  
    return {"data": data};
  }

  // 初始化
  createHorseCompetitors(); 
  createPlayers(); 
  
  const submitBtn = document.getElementById('submitBtn');
  const resultDiv = document.getElementById('result');

  submitBtn.addEventListener('click', async () => {

    const requestBody = getInputValuesAsBody();
    console.log(requestBody)
    // resultDiv.innerHTML = `<p style="">Hello World!</p>`;
    // resultDiv.textContent = JSON.stringify(result, null, 2);
    
    // 發送 POST 請求
    try {
      const response = await fetch('http://127.0.0.1:8000/api/predictor/', {
        mode: 'no-cors',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });
      // TODO: haven't get answer
      console.log(response)

      // 獲取並解析回應
      const responseData = await response.json();
      console.log("Response:", responseData);
  
      // 渲染回應在頁面上
      resultDiv.innerHTML = `<pre>${JSON.stringify(responseData, null, 2)}</pre>`;
    } catch (error) {
      console.error('Error:', error);
      resultDiv.innerHTML = `<p style="color: red;">Error fetching data.</p>`;
    }
  });