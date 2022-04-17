import './App.css'
import axios from "axios" 
import { useEffect, useState } from 'react'

function App() {
  const [classname, setClassName] = useState("")
  const [img, setImg] = useState('');
  const [imgFile,setImgFile] = useState();

  const [isImageUpload, setIsImageUpload] = useState(false)

  useEffect(() => {
    if(isImageUpload) {
      const reader = new FileReader()
      reader.onload = () => {
        if (reader.readyState === 2) {
          setImg(reader.result)
        }
      }
      reader.readAsDataURL(imgFile)
    }
  },[isImageUpload])


  const onFileChange = (e) => {
    console.log(e.target.files[0])
    
    if(e.target && e.target.files[0]) {
      setImgFile(e.target.files[0])
      setIsImageUpload(true)
    }

    

  }

  const SubmitFileData = () => {
    let formData = new FormData()
    formData.append('file', imgFile)
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
    <div className='App'>
      <div>
        <input type='file' name='file_upload' onChange={onFileChange} />
        <button onClick={SubmitFileData}>Predict</button>
      </div>
      <div>
        <img src={img} alt='' />
      </div>
      <div>Class: {classname}</div>
    </div>
  )
}

export default App;
