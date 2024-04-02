import About from "./components/About";
import Hero from "./components/Hero";
import Navbar from "./components/Navbar";
import Skills from "./components/Skills";
import Work from "./components/Work";

function App() {
  return (
    <div className="App">
        <Navbar />
        <Hero />
        <Skills />
        <About />
        <Work />
    </div>
  );
}

export default App;
