import "./Menu.css"

import { useEffect, useState } from "react"

interface Product {
  name: string
  price: number
  image: string
}

export function Menu() {
  const [ products, setProducts ] = useState<Product[]>([])

  useEffect(() => {
    const apiUrl = new URL("http://localhost:8001/api/v1/products")

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        setProducts(data)
      })
      .catch(error => console.warn(error))
  }, [])
  
  return (
    <div className="menu">
      <h2>Cardápio</h2>
      <ul>
        { products.map(product => {
          return (
            <img src={ product.image } alt="" />
            // <div className="product-card">
            //   <li key={ product.name }>{ product.name } - { product.price }</li>
            // </div>
          )
        })}
      </ul>
    </div>
  )
}
