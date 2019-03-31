package space

// planet_information struct for seconds and days
type planetInformation struct {
	year float64
}

// Planet is a tring type
type Planet string

const earthSeconds = 31557600

var m = map[Planet]planetInformation{
	"Earth": planetInformation{
		1 * earthSeconds,
	},
	"Mercury": planetInformation{
		0.2408467 * earthSeconds,
	},
	"Venus": planetInformation{
		0.61519726 * earthSeconds,
	},
	"Mars": planetInformation{
		1.8808158 * earthSeconds,
	},
	"Jupiter": planetInformation{
		11.862615 * earthSeconds,
	},
	"Saturn": planetInformation{
		29.447498 * earthSeconds,
	},
	"Uranus": planetInformation{
		84.016846 * earthSeconds,
	},
	"Neptune": planetInformation{
		164.79132 * earthSeconds,
	},
}

// Age is a func to determine the age beside orbital period of a planet
func Age(seconds float64, planet Planet) float64 {
	return seconds / m[planet].year
}
