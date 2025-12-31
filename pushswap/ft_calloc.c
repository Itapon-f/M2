/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: itapon-f <itapon-f@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 13:10:00 by itapon-f          #+#    #+#             */
/*   Updated: 2025/12/29 14:39:29 by itapon-f         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	*ptr;
	size_t			count;

	ptr = (unsigned char *)s;
	count = 0;
	while (count < n)
	{
		ptr[count] = (unsigned char)c;
		count ++;
	}
	return (s);
}

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*element;

	if (size != 0 && nmemb > SIZE_MAX / size)
		return (NULL);
	if (nmemb > INT_MAX || size > INT_MAX)
		return (malloc(0));
	element = malloc(nmemb * size);
	if (!element)
		return (0);
	ft_memset(element, 0, nmemb * size);
	return (element);
}
