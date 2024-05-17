import "./Sponsor.css"

import { useEffect, useState } from "react"

interface Sponsor {
  name: string
  url_social_media: string
  image: string
}


export function Sponsor(): JSX.Element {
  const [ sponsors, setSponsors ] = useState<Sponsor[]>([])

  useEffect(() => {
    const apiUrl = new URL(`${import.meta.env.VITE_API_URL}/api/v1/sponsors`)

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        setSponsors(shuffle(data))
      })
      .catch(error => console.warn(error))
  }, [])

  return (
    <section className="sponsors">
      <h2>Patrocinadores</h2>
      <div className="sponsors-container">
        { sponsors.map(sponsor => {
          return (
            <div className="sponsor-card" key={ sponsor.name }>
              <a href={ sponsor.url_social_media } target="_blank">
                <img src={ sponsor.image } />
              </a>
            </div>
          )
        })}
      </div>
    </section>
  )
}

function shuffle(array: Sponsor[]): Sponsor[] {
  let newArray: Sponsor[] = []
  let randomIndex: number

  while (array.length > 0) {
    randomIndex = Math.floor(Math.random() * array.length)
    let itemData = array.splice(randomIndex, 1)[0]
    newArray.push(itemData)
  }
  return newArray
}
