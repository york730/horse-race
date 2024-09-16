// TODO: 6 horses value
// TODO: compose to a body
// TODO: call API
// TODO: get response and render

const horses = {
    '1': '3, 4',
    '2': '1, 2, 6',
    '3': '3, 5, 6',
    '4': '4, 5',
    '5': '3, 4',
    '6': '2, 4, 6'
  };

const horseList = document.getElementById('horseList');
const submitBtn = document.getElementById('submitBtn');
const resultDiv = document.getElementById('result');

for (let key in horses) {
    const div = document.createElement('div');
    div.classList.add('horse-item');
    div.innerHTML = `<label>${key}: </label><input type="text" class="input-field" id="input-${key}" value="${horses[key]}" />`;
    horseList.appendChild(div);
  }

  submitBtn.addEventListener('click', async () => {
    const requestBody = {};
    resultDiv.innerHTML = `<p style="">Hello World!</p>`;
    
    // 發送 POST 請求
    // try {
    //   const response = await fetch('https://your-api-url.com/endpoint', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(requestBody)
    //   });
  
    //   // 獲取並解析回應
    //   const responseData = await response.json();
    //   console.log("Response:", responseData);
  
    //   // 渲染回應在頁面上
    //   resultDiv.innerHTML = `<pre>${JSON.stringify(responseData, null, 2)}</pre>`;
    // } catch (error) {
    //   console.error('Error:', error);
    //   resultDiv.innerHTML = `<p style="color: red;">Error fetching data.</p>`;
    // }
  });