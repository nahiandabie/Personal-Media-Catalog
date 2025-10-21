<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <title>Personal Media Catalog</title>
        <style>
          body { font-family: Arial; margin: 20px; }
          h1 { color: #0055aa; }
          table { border-collapse: collapse; width: 100%; }
          th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
          th { background-color: #f2f2f2; }
        </style>
      </head>
      <body>
        <h1>Personal Media Catalog</h1>
        <table>
          <tr>
            <th>Type</th>
            <th>Title</th>
            <th>Year</th>
            <th>Genre</th>
            <th>Details</th>
          </tr>
          <xsl:for-each select="catalog/*">
            <tr>
              <td><xsl:value-of select="name()"/></td>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="year"/></td>
              <td><xsl:value-of select="genre"/></td>
              <td>
                <xsl:choose>
                  <xsl:when test="name() = 'book'">
                    Author: <xsl:value-of select="author"/> (<xsl:value-of select="pages"/> pages)
                  </xsl:when>
                  <xsl:when test="name() = 'movie'">
                    Director: <xsl:value-of select="director"/>, Duration: <xsl:value-of select="duration"/>
                  </xsl:when>
                  <xsl:when test="name() = 'videogame'">
                    Platform: <xsl:value-of select="platform"/>, Developer: <xsl:value-of select="developer"/>
                  </xsl:when>
                </xsl:choose>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
