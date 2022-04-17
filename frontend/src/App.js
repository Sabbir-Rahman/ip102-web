import './App.css'
import axios from "axios"
import { useState } from 'react'

function App() {
  let formData = new FormData()
  const [classname, setClassName] = useState("")

  const onFileChange = (e) => {
    console.log(e.target.files[0])

    if(e.target && e.target.files[0]) {
      formData.append("file", e.target.files[0])
    }
  }

  const SubmitFileData = () => {
    axios.post('http://127.0.0.1:5000/predict', formData)
    .then(res => {
      console.log(res.data)
      setClassName(res.data.class_name)
    })
    .catch(error => {
      console.log(error)
    })
  }

  return (
    <div className="App">
      <div>
        <input type="file" name="file_upload" onChange={onFileChange} />
      </div>
      <div>
        <button onClick={SubmitFileData}>Submit Button</button>
      </div>
      <div>
        Class: {classname}
      </div>
    </div>
  );
}

export default App;
