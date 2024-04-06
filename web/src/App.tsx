import "./App.css"

import { Header } from "./components/Header"
import { Menu } from "./components/Menu"
import { Sponsor } from "./components/Sponsor"

function App() {
  return (
    <div className="container">
      <Header />
      <Menu />
      <Sponsor />
    </div>
  )
}

export default App
