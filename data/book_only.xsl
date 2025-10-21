<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <title>Book Catalog</title>
        <style>
          body { font-family: Arial; margin: 20px; }
          h1 { color: #cc0000; }
          table { border-collapse: collapse; width: 100%; }
          th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
          th { background-color: #f9f9f9; }
        </style>
      </head>
      <body>
        <h1>Book Catalog</h1>
        <table>
          <tr>
            <th>Title</th>
            <th>Year</th>
            <th>Genre</th>
            <th>Author</th>
            <th>Pages</th>
          </tr>
          <xsl:for-each select="catalog/book">
            <tr>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="year"/></td>
              <td><xsl:value-of select="genre"/></td>
              <td><xsl:value-of select="author"/></td>
              <td><xsl:value-of select="pages"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
