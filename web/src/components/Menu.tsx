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
    <section className="products">
      <h2>Cardápio</h2>
      <div className="menu">
        { products.map(product => {
          return (
            <div className="product-card" key={ product.name }>
              <div className="image-box">
                <img src={ product.image } alt="" />
              </div>
              <div className="product-description">
                <p>{ product.name }</p>
                <p>R$ { product.price.toString().replace(".", ",") }</p>
              </div>
            </div>
          )
        })}
      </div>
    </section>
  )
}
