import './App.css';

function App() {

  const onFileChange = (e) => {
    console.log(e.target.files[0])
  }

  return (
    <div className="App">
      <div>
        <input type="file" name="file_upload" onChange={onFileChange} />
      </div>
      <div>
        <button>Submit Button</button>
      </div>
    </div>
  );
}

export default App;
