import "./Sponsor.css"

import { useEffect, useState } from "react"

interface Sponsor {
  name: string
  url_social_media: string
  image: string
}


export function Sponsor() {
  const [ sponsors, setSponsors ] = useState<Sponsor[]>([])

  useEffect(() => {
    const apiUrl = new URL("http://localhost:8001/api/v1/sponsors")

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        setSponsors(data)
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
