import { useEffect, useState } from "react"

interface Product {
  name: string
  price: number
}

export function Menu() {
  const [ products, setProducts ] = useState<Product[]>([])

  useEffect(() => {
    const apiUrl = new URL("http://localhost:8000/api/v1/products")

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        setProducts(data)
      })
      .catch(error => console.warn(error))
  }, [])
  
  return (
    <>
      <h1>Menu</h1>
      <ul>
        { products.map(product => {
          return (
            <li key={ product.name }>{ product.name } - { product.price }</li>
          )
        })}
      </ul>
    </>
  )
}
