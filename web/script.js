
// 通常要取出到constant，但有點懶 :p
// API 的網址
// const requestURL = 'http://127.0.0.1:8000/api/predictor/'
const requestURL = 'https://playground-eight-psi.vercel.app/api/predictor/'


// 有多少馬匹跟他們的固定數值。
const horses = {
  '1': [3, 4],
  '2': [1, 2, 6],
  '3': [3, 5, 6],
  '4': [4, 5],
  '5': [3, 4],
  '6': [2, 4, 6]
};

const allHorse = Array.from({ length: Object.keys(horses).length }, (v, i) => i + 1);

const requestBodyIndex = ["一號", "二號", "三號", "四號"]

// id: horseList, 根據有幾個馬匹生成跟渲染 3 cols 的內容。
function createHorseCompetitors() {

  const horseList = document.getElementById('horseList');

  for (let key in horses) {
    const div = document.createElement('div');
    div.classList.add('horse-item');
    div.innerHTML = `<div class="flex border-color horse-background text-base text-center"><div class="horse-label-background font-white-color horse-padding border-radius-5">${key}</div><div class="font-coffee-color horse-padding" id="horse-${key}">${horses[key]}</div> </div>`;
    horseList.appendChild(div);
  }

}

// id: raceList, 生產四個賽道、指定的出賽馬匹、六個道具、一個押金
function createPlayers() {
  const container = document.getElementById("raceList");

  // For loop 四個賽代
  for (let i = 1; i <= 4; i++) {
    // 創建最外層 div，用display flex 屬性讓 指定的出賽馬匹、六個道具、一個押金 成一列。
    const flexDiv = document.createElement("div");
    flexDiv.className = "flex justify-center gap-35 text-base";

    // 第一個 div 是出賽馬匹，用flex 包是因為我需要將馬匹的選擇方塊的高度縮小後，將他垂直置中，我不希望他滿版。
    const input1Div = document.createElement("div");
    input1Div.className = "flex flex-align-center";

    const select = document.createElement("select");
    select.id = `select-${i}`;
    select.className = "horse-background font-coffee-color competitor-label-padding border-color text-sm"

    // 沒做到拖拉的功能，直接用下拉式選單代替 :p，因此根據有幾匹馬來渲染幾個選項。
    allHorse.forEach((horse, index) => {
      const option = document.createElement("option");
      option.value = horse;
      option.text = `${horse}`;
      // 設定第幾個選項為預設值 (或根據條件動態設置)
      if (index === (i-1)) {
        option.selected = true; 
      }

      select.appendChild(option);
    });
    
    input1Div.appendChild(select);

    // 第二個div是要包含六個道具，也是用flex 去包住六個道具的 input
    const stretchDiv1 = document.createElement("div");
    stretchDiv1.className = "flex flex-align-center";

    for (let j = 2; j <= 7; j++) {
      // 一個道具輸入的div (包含輸入框跟加減按鈕)
      const numberInputDiv = document.createElement("div");
      numberInputDiv.className = "number-input"

      // 創建減少數字按鈕
      const minusButton = document.createElement("button");
      minusButton.textContent = "-";
      minusButton.className = "minus";
      minusButton.onclick = function() {
        input.stepDown(); // 減少數字
      };

      // 創建增加數字按鈕
      const plusButton = document.createElement("button");
      plusButton.textContent = "+";
      plusButton.className = "plus";
      plusButton.onclick = function() {
        input.stepUp(); // 增加數字
      };

      // 創建輸入數字的文字框
      const input = document.createElement("input");
      input.type = "number";
      input.value = 0;
      input.min = 0;
      input.max = 10;
      input.id = `input-${i}-${j}`; // 動態生成id
      
      numberInputDiv.appendChild(plusButton);
      numberInputDiv.appendChild(input);
      numberInputDiv.appendChild(minusButton);
      
      stretchDiv1.appendChild(numberInputDiv);
    }

    // 創建最後一個是押金的div，一樣用flex 包，也是因為我需要輸入的方塊高度縮小後，將他垂直置中，我不希望他滿版。
    const stretchDiv2 = document.createElement("div");
    stretchDiv2.className = "flex flex-align-center";

    // 輸入金額的文字框
    const input2 = document.createElement("input");
    input2.type = "number";
    input2.min = 0;
    input2.max = 10000;
    input2.value = 1;
    input2.id = `input-${i}-8`; // 動態生成id
    input2.className = "h-50 w-input-3 border-color text-center text-sm heading-color"
    stretchDiv2.appendChild(input2);

    // 將所有子元素加入外層 div: 賽道、出賽的馬匹、道具、押金
    flexDiv.appendChild(input1Div);
    flexDiv.appendChild(stretchDiv1);
    flexDiv.appendChild(stretchDiv2);

    // 將外層 div 加入 raceList
    container.appendChild(flexDiv);
  }
}

  // 取得所有 input 值並組成 JSON
  function getInputValuesAsBody() {
    const userInputs = document.querySelectorAll("input[type='number'], select");
    const values = {};

    userInputs.forEach((input) => {
      values[input.id] = input.value || 0; // 如果輸入為空值，預設為0
    });

    const data = {};
    for (let i = 1; i <= 4; i++) {
      const horseValue = horses[values[`select-${i}`]];
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

  // id: submitBtn
  // 1. 按下submitBtn按鈕後會先透過函式 getInputValuesAsBody 收集所有input的資料。
  // 2. 接著透過fetch 搭配 async call API
  // 3. 取得response data 後 id: result div 渲染預測內容。
  submitBtn.addEventListener('click', async () => {

    const requestBody = getInputValuesAsBody();
    
    // 發送 POST 請求
    try {
      const response = await fetch(requestURL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      const responseData = await response.json();
      const data = responseData.data
      resultDiv.innerHTML = '';

      for (let i = 0; i < data.length; i++) {
        const item = data[i];
      
        const itemDiv = document.createElement("div");
      
        itemDiv.innerHTML = `
          ${item}
        `;
      
        resultDiv.appendChild(itemDiv);
      }

    } catch (error) {
      console.error('Error:', error);
      resultDiv.innerHTML = `<p style="color: red;">Error fetching data.</p>`;
    }
  });