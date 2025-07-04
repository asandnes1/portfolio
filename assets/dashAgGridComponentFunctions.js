var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});
    
  dagcomponentfuncs.CompanyLogoRenderer = function (props) {
    var url = "https://www.ag-grid.com/example-assets/space-company-logos/" + props.value.toLowerCase() + ".png";
    return React.createElement(
      "span",
      null,
      React.createElement("img", { src: url, style: { width: "25px", height: "auto", filter: "brightness(1.1)" } }),
      React.createElement("span", { style: { paddingLeft: "4px" } }, props.value)
    );
  }


  // Use this file to change the style of AgGrid components.
  